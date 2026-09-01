# Canvas pages: weekly overview pages ("veckoöversikt") generated from the
# TimeEdit schedule and pushed with canvaslms.  Included from ./Makefile.
#
#   make schedule          regenerate the schedule block in all PAGES
#   make update-schedule   re-download the ICS first, then regenerate
#   make push-pages        push changed PAGES to Canvas (existing pages only)
#   make create-pages      one-shot: create the pages in Canvas the first time
#   make create-modules    one-shot: create the Canvas modules in canvas-modules.txt
#
# COURSE is the nytid nickname (schedule, course code); CANVAS_COURSE is the
# canvaslms course regex and defaults to COURSE.  To rehearse in a sandbox:
#   make create-modules create-pages CANVAS_COURSE='^Sandbox dbosk$'
#
# The pages are the source of truth: Canvas strips the HTML-comment markers
# that veckoschema.py uses, so never pull these pages back from Canvas.

COURSE?=	prgi26
CANVAS_COURSE?=	${COURSE}
ICS_URL?=	$(shell nytid courses config ${COURSE} ics | sed 's/^ics = //')
ICS?=		schedule.ics
VECKOSCHEMA?=	bin/veckoschema.py

# Canvas modules in course order (one per line); one page goes first in each.
MODULES_FILE?=	canvas-modules.txt

# Week pages get their schedule block filled by veckoschema.py ...
WEEK_PAGES+=	modules/helloworld/vecka.md
WEEK_PAGES+=	modules/variables/vecka.md
WEEK_PAGES+=	modules/conditionals/vecka.md
WEEK_PAGES+=	modules/iterations/vecka.md
WEEK_PAGES+=	modules/classes/vecka.md
WEEK_PAGES+=	modules/containers/vecka.md
WEEK_PAGES+=	modules/files/vecka.md
WEEK_PAGES+=	modules/graphics/vecka.md
WEEK_PAGES+=	modules/overview/vecka-datorprov.md
WEEK_PAGES+=	modules/project/vecka.md
# ... while these are pushed as they are.
PAGES+=		modules/overview/pythondelen.md
PAGES+=		${WEEK_PAGES}

${ICS}:
	curl -fsS "${ICS_URL}" -o $@.tmp && mv $@.tmp $@

${VECKOSCHEMA}: $(dir ${VECKOSCHEMA})veckoschema.nw
	${MAKE} -C $(dir ${VECKOSCHEMA}) $(notdir ${VECKOSCHEMA})

.PHONY: schedule
schedule: ${ICS} ${VECKOSCHEMA}
	python3 ${VECKOSCHEMA} --course ${COURSE} --ics ${ICS} --in-place ${WEEK_PAGES}

.PHONY: update-schedule
update-schedule:
	${RM} ${ICS}
	${MAKE} schedule

PUSH_STAMPDIR_PAGES:=	.pushed-pages.d/$(shell printf '%s' '${CANVAS_COURSE}' | tr -c 'A-Za-z0-9' _)

.PHONY: push-pages
push-pages: $(addprefix ${PUSH_STAMPDIR_PAGES}/,${PAGES})

${PUSH_STAMPDIR_PAGES}/%: %
	@mkdir -p $(dir $@)
	canvaslms pages edit -c "${CANVAS_COURSE}" -f "$<"
	@touch $@

.PHONY: create-pages
create-pages:
	for page in ${PAGES}; do \
		echo "Creating $$page in ${CANVAS_COURSE} ..."; \
		canvaslms pages edit --create -c "${CANVAS_COURSE}" -f "$$page" || exit 1; \
	done

# Modules are created in file order and appended after the existing ones;
# canvaslms refuses a duplicate name unless --allow-duplicate is given, so
# existing modules are reported and skipped rather than duplicated.
.PHONY: create-modules
create-modules: ${MODULES_FILE}
	@while IFS= read -r module; do \
		[ -n "$$module" ] || continue; \
		echo "Creating module '$$module' in ${CANVAS_COURSE} ..."; \
		canvaslms modules create -c "${CANVAS_COURSE}" "$$module" \
			|| echo "  (skipped: $$module)"; \
	done < ${MODULES_FILE}

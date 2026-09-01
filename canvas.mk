# Canvas pages: weekly overview pages ("veckoöversikt") generated from the
# TimeEdit schedule and pushed with canvaslms.  Included from ./Makefile.
#
#   make schedule          regenerate the schedule block in all PAGES
#   make update-schedule   re-download the ICS first, then regenerate
#   make push-pages        push changed PAGES to Canvas (existing pages only)
#   make create-pages      one-shot: create the pages in Canvas the first time
#
# The pages are the source of truth: Canvas strips the HTML-comment markers
# that veckoschema.py uses, so never pull these pages back from Canvas.

COURSE?=	prgi26
ICS_URL?=	$(shell nytid courses config ${COURSE} ics | sed 's/^ics = //')
ICS?=		schedule.ics
VECKOSCHEMA?=	bin/veckoschema.py

PAGES+=		modules/helloworld/vecka.md
PAGES+=		modules/variables/vecka.md
PAGES+=		modules/conditionals/vecka.md
PAGES+=		modules/iterations/vecka.md
PAGES+=		modules/classes/vecka.md
PAGES+=		modules/containers/vecka.md
PAGES+=		modules/files/vecka.md
PAGES+=		modules/graphics/vecka.md
PAGES+=		modules/overview/vecka-datorprov.md
PAGES+=		modules/project/vecka.md

${ICS}:
	curl -fsS "${ICS_URL}" -o $@.tmp && mv $@.tmp $@

${VECKOSCHEMA}: $(dir ${VECKOSCHEMA})veckoschema.nw
	${MAKE} -C $(dir ${VECKOSCHEMA}) $(notdir ${VECKOSCHEMA})

.PHONY: schedule
schedule: ${ICS} ${VECKOSCHEMA}
	python3 ${VECKOSCHEMA} --course ${COURSE} --ics ${ICS} --in-place ${PAGES}

.PHONY: update-schedule
update-schedule:
	${RM} ${ICS}
	${MAKE} schedule

PUSH_STAMPDIR_PAGES:=	.pushed-pages.d

.PHONY: push-pages
push-pages: $(addprefix ${PUSH_STAMPDIR_PAGES}/,${PAGES})

${PUSH_STAMPDIR_PAGES}/%: %
	@mkdir -p $(dir $@)
	canvaslms pages edit -c "${COURSE}" -f "$<"
	@touch $@

.PHONY: create-pages
create-pages:
	for page in ${PAGES}; do \
		echo "Creating $$page in ${COURSE} ..."; \
		canvaslms pages edit --create -c "${COURSE}" -f "$$page" || exit 1; \
	done

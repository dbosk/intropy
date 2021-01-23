function rot = newton(x_start, func, funcp)
tolerance = 0.5e-8; %Vilket fel vi väljer att acceptera

error = 1; %sätter startvärde för error så att loopen startas

while error > tolerance
    delta = func(x_start) / funcp(x_start); %för att göra koden mer lättläst
    x_new = x_start - delta; %detta är newton-rhapsons
    error = abs(delta/x_new); %det relativa felet
    x_start = x_new; %x_new blir nu den nya gissningen
end
rot = x_new; %returnerar det sista x_new
end


%Ritar funktionen z = x^2*y^2
clf  %clear figure
x = 0:1:5*pi;
y = -6:1:6;
[X,Y] = meshgrid(x,y);
Z = sin(X).*sin(Y)
surf(X,Y,Z)
title("sin(x)*sin(y)")
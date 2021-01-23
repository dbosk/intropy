
%% Lösa ekvationssystemet
clc, clear variables;
%Löser Ax = b
 
 A =[2 1 3; 5 0 1; -1 -1 -3];
 b = [13;8;-12];
 
 x = A\b
 
 %% Plotta funktionerna
 clc, clear variables
%Funktionerna:
f1= @(x)(x.^6-21*x.^5+175*x.^4-735*x.^3+1624*x.^2-1764*x+720);
f2 = @(x)(x.^6+21*x.^5+175*x.^4+735*x.^3+1624*x.^2+1764*x+720);
f3 = @(x)(x.^6+3*x.^5-41*x.^4-87*x.^3+400*x.^2+444*x-720);
f4= @(x)(x.^6-3*x.^5-41*x.^4+87*x.^3+400*x.^2-444*x-720);

%Intervall på x-axeln:
xint = [-6 6]

%I varsin figur
figure(1)
fplot(f1, xint)

figure(2)
fplot(f2, xint)

figure(3)
fplot(f3, xint)

figure(4)
fplot(f4, xint)

%I samma figur
fplot(f1, xint, 'r')
hold on
fplot(f2, xint, 'g')
hold on
fplot(f3, xint, 'b')
hold on
fplot(f4, xint, 'y')
hold on

 %% Hitta rötterna mha Newton Rhapsons%%
 
clc, clear variables
format long;

%f= @(x)(x.^6-21*x.^5+175*x.^4-735*x.^3+1624*x.^2-1764*x+720);
%fp = @(x)(6*x.^5 - 105*x.^4 + 700*x.^3 - 2205*x.^2 + 3248*x - 1764);

%f = @(x)(x.^6+21*x.^5+175*x.^4+735*x.^3+1624*x.^2+1764*x+720);
%fp = @(x)(6*x.^5 + 105*x.^4 + 700*x.^3 + 2205*x.^2 + 3248*x + 1764);

%f = @(x)(x.^6+3*x.^5-41*x.^4-87*x.^3+400*x.^2+444*x-720);
%fp = @(x)(6*x.^5+15*x.^4-164*x.^3-261*x.^2+800*x+444);

f = @(x)(x.^6-3*x.^5-41*x.^4+87*x.^3+400*x.^2-444*x-720);
fp = @(x)(6*x.^5-15*x.^4-164*x.^3+261*x.^2+800*x-444);

start_guess = -6;

disp('En rot till funktionen är...')

rot = newton(start_guess, f, fp)


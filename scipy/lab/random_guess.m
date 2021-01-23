function roots = random_guess(func, funcp)

roots = [];

while length(roots) ~= 6 
    start_guess = rand();
    root = newton(start_guess, func, funcp);
    root = round(root);
    
    if ismember(root, roots) ~= 1
        roots = [roots root];
    end
    
  
end

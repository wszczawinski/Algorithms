const factorial = (num: number): number => {
  if (num === 1) {
    return 1;
  }

  return num * factorial(num - 1);
};

const x = 5;

console.log(`Factorial of ${x} is:`, factorial(5));

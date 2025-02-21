const linearSearch = (arr: number[], needle: number): boolean => {
  for (const element of arr) {
    if (element === needle) {
      return true;
    }
  }

  return false;
};

console.log(linearSearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 7));

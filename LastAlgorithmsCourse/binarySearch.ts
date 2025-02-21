const binarySearch = ({ arr, x }: { arr: number[]; x: number }): boolean => {
  let lo = 0;
  let hi = arr.length;

  while (lo < hi) {
    const mid = Math.floor((lo + hi) / 2);
    const currentValue = arr[mid];

    if (currentValue === x) {
      return true;
    } else if (currentValue > x) {
      hi = mid;
    } else {
      lo = mid + 1;
    }
  }

  return false;
};

const heyStack = [0, 1, 2, 3, 4, 5, 6, 7, 8];
const needle = 8;

console.log(binarySearch({ arr: heyStack, x: needle }));

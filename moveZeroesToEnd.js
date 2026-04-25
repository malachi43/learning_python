const arr = [1, 2, 0, 3, 0, 0, 5, 0, 7, 9, 0];

function moveZerosToEnd(arr) {
  console.log("original_array -> ", arr)
  const clone = arr.slice();
  //find the first occurence of zero
  let count = 0;
  let k = -1;

  while (count < clone.length) {
    if (clone[count] == 0) {
      k = count;
      //exist immediately from the loop
      break;
    }
    ++count;
  }

  if (k == -1) return clone; // the loop contains no zero, if the value of k is still -1

  for (let j = k + 1; j < clone.length; j++) {
    if (clone[j] != 0) {
      swap(clone, j, k);
      ++k;
    }
  }

  return clone;
}


function swap(arr, idx1, idx2) {
  const temp = arr[idx1];
  arr[idx1] = arr[idx2];
  arr[idx2] = temp;
}

console.log("array_with_zeros_moved_to_the_end -> ", moveZerosToEnd(arr))

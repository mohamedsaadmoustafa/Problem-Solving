function* fibGenerator() {
  let arr = [0, 1];

  while (true) {
    yield arr[0];
    let tmp = arr[0];
    arr[0] = arr[1];
    arr[1] += tmp;
  }
}

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */

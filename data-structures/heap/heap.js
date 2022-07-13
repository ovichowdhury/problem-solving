class Heap {
  arr = [];
  type = "MIN";
  constructor(type = "MIN") {
    this.type = type;
  }

  insert(item) {
    if (typeof item === "number") {
      this.arr.push(item);
      this.upHeapify(this.arr.length - 1);
    } else throw new TypeError("Invalid Data Type");
  }

  delete(index) {
    if (typeof index === "number" && index < this.arr.length) {
      this.swap(index, this.arr.length - 1);
      this.arr.pop();
      this.downHeapify(index);
    } else throw new TypeError("Invalid Data Type");
  }

  downHeapify(parent) {
    let pivot = parent;
    const left = 2 * parent + 1;
    const right = 2 * parent + 2;
    let conditionLeft = false;
    conditionLeft =
      this.type === "MIN"
        ? left < this.arr.length && this.arr[pivot] > this.arr[left]
        : left < this.arr.length && this.arr[pivot] < this.arr[left];
    if (conditionLeft) pivot = left;

    let conditionRight = false;
    conditionRight =
      this.type === "MIN"
        ? right < this.arr.length && this.arr[pivot] > this.arr[right]
        : right < this.arr.length && this.arr[pivot] < this.arr[right];
    if (conditionRight) pivot = right;

    if (parent !== pivot) {
      this.swap(parent, pivot);
      this.downHeapify(pivot);
    }
  }

  upHeapify(childIndex) {
    const parentIndex = Math.floor((childIndex - 1) / 2);
    let condition = false;
    condition =
      this.type === "MIN"
        ? this.arr[parentIndex] > this.arr[childIndex]
        : this.arr[parentIndex] < this.arr[childIndex];
    if (condition) {
      this.swap(parentIndex, childIndex);
      this.upHeapify(parentIndex);
    }
  }

  swap(index1, index2) {
    if (
      index1 >= 0 &&
      index1 < this.arr.length &&
      index2 >= 0 &&
      index2 < this.arr.length &&
      index1 != index2
    ) {
      const temp = this.arr[index1];
      this.arr[index1] = this.arr[index2];
      this.arr[index2] = temp;
    }
  }
}

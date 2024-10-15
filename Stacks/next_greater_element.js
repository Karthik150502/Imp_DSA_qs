function nextGreaterNumber(nums1, nums2) {

    let hashM = {}
    let res = new Array(nums1.length).fill(-1);
    nums1.forEach((element, index) => {
        hashM[element] = index
    });

    let stack = []
    nums2.forEach((num) => {
        while (stack && stack[stack.length - 1] < num) {
            let last_num = stack.pop()
            if (last_num in hashM) {
                res[hashM[last_num]] = num
            }
        }
        stack.push(num)
    })

    return res
}



let n1 = [4, 1, 2]
let n2 = [1, 3, 4, 2]
let res = nextGreaterNumber(n1, n2)
console.log(res);


pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32){
    let mut new_nums: Vec<i32> = Vec::new();
    for i in 0..m{
        new_nums.push(nums1[i as usize]);
    }
    for i in 0..n{
        new_nums.push(nums2[i as usize]);
    }
    new_nums.sort();
    *nums1 = new_nums;
    println!("{:?}", nums1);
}


pub fn merge_two(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32){
    *nums1 = nums1[0..m as usize].to_vec();
    *nums2 = nums2[0..n as usize].to_vec();
    nums1.append(nums2);
    nums1.sort();
    println!("{:?}", nums1);
}


fn main() {
    let mut nums1 = vec![1,2,3,0,0,0];
    let mut nums2 = vec![2,5,6];
    merge_two(nums1.as_mut(), 3, nums2.as_mut(), 3);
}

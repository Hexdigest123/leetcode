// general solution
fn single_number(nums: Vec<i32>) -> i32{
    let mut r= 0;
    for num in nums {
        r ^= num;
    }
    r
}

// more memory efficient solution
fn single_number_two(nums: Vec<i32>) -> i32{
    nums.into_iter().fold(0, |acc, x| acc ^ x)
}

fn main() {
   println!("{}", single_number_two(vec![2,2,1,3,3,4,4,]));
}

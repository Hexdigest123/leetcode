pub fn climb_stairs(n: i32) -> i32{
    let n = n as usize;
    let mut dp = vec![0; n + 1];
    dp[0] = 1;
    dp[1] = 1;
    for i in 2..=n {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    dp[n]
}
fn main() {
    println!("{}", climb_stairs(3));
    println!("{}", climb_stairs(2));
    println!("{}", climb_stairs(4));
}

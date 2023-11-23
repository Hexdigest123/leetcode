
pub fn my_sqrt(x: i32) -> i32{
    let y = x as f64;
    y.sqrt() as i32
}
fn main() {
    println!("{}", my_sqrt(9));
}

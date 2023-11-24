pub fn add_binary(a: String, b: String) -> String{
    let mut a_chars: Vec<char> = a.chars().collect();
    let mut b_chars: Vec<char> = b.chars().collect();
    a_chars.reverse();
    b_chars.reverse();

    let mut carry = 0;
    let mut result = String::new();

    for i in 0..a_chars.len().max(b_chars.len()) {

        let sum = if i < a_chars.len() { a_chars[i].to_digit(10).unwrap() } else { 0 } +
            if i < b_chars.len() { b_chars[i].to_digit(10).unwrap() } else { 0 } + carry;
        result.push_str(&(sum % 2).to_string());
        carry = sum / 2;
    }

    if carry > 0 {
        result.push_str(&carry.to_string());
    }

    result.chars().rev().collect()
}

fn main() {
    println!("{}", add_binary("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101".to_string(),
                              "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011".to_string()));
}

fn main() {
    let mut count =0;
loop{
    count = count +1;
    if count == 3{
        println!("basic loop completed");
        break;
    }
}
while count != 3{
    count =count +1;
    println!("{}" ,count);
    
}
println!("while loop completed");

for x in 1..=3{
    println!("{}", x);
}
println!("for loop completed");
}

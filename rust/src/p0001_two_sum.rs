use std::collection::HashMap;

pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32>{
    let mut seen = HashMap::new();

    for (i, num) in nums.iter().enumerate(){
        let complement = target - num;
        if seen.contains(complement){
            return [seen[complement, i]
        }else{
            seen.insert(item, i);
        }
    }

}
package se.callistaenterprise.kata.fizzbuzz;

import java.util.ArrayList;
import java.util.List;

public class FizzBuzz {

	public List<String> listOutput() {
		
		List<Integer> numbers = new ArrayList<Integer>();//Arrays.asList(1,2,3);
		
		FunnyNumberFormatter fnm = new FunnyNumberFormatter();
		
		for(int i=1; i<=100; ++i) 
			numbers.add(new Integer(i));
		
		return fnm.format(numbers); 
	}
	
	public void print() {
		for (String list : listOutput()) {
			System.out.println(list);
		}
	}


}

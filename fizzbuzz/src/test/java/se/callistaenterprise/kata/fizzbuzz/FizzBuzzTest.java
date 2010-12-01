package se.callistaenterprise.kata.fizzbuzz;

import junit.framework.Assert;

import org.junit.Test;

import se.callistaenterprise.kata.fizzbuzz.FizzBuzz;


public class FizzBuzzTest {
	
	private FizzBuzz fizzBuzz = new FizzBuzz();

	@Test
	public void checkFirstItemIs1() {
		Assert.assertEquals("1", fizzBuzz.listOutput().get(0));
	}
	
	@Test 
	public void checkFirstFizz() {
		Assert.assertEquals("Fizz", fizzBuzz.listOutput().get(2));
	}

	@Test 
	public void checkFirstBuzz() {
		Assert.assertEquals("Buzz", fizzBuzz.listOutput().get(4));
	}

	
	@Test
	public void checkSize() {
		Assert.assertEquals("100!", 100, fizzBuzz.listOutput().size());
	}
	
	@Test
	public void noTest_insteadOfMain() {
		fizzBuzz.print();
	}
	
	
	
	
}

package se.callistaenterprise.kata.fizzbuzz;

import static junit.framework.Assert.assertFalse;
import static junit.framework.Assert.assertTrue;

import org.junit.Assert;
import org.junit.Test;

import se.callistaenterprise.kata.fizzbuzz.FunnyNumberFormatter;


public class FunnyNumberFormatterTest {
	
	
	private FunnyNumberFormatter funnyNumberFormatter = new FunnyNumberFormatter();

	@Test 
	public void checkThreeIsFizz() {
		assertTrue(funnyNumberFormatter.isFizz(3));
	}
	@Test 
	public void checkTwoIsNotFizz() {
		assertFalse(funnyNumberFormatter.isFizz(2));
	}
	
	@Test 
	public void checkFifteenIsFizz() {
		assertTrue(funnyNumberFormatter.isFizz(15));
	}	
	
	@Test 
	public void checkFifteenIsBuzz() {
		assertTrue(funnyNumberFormatter.isBuzz(15));
	}
	
	@Test
	public void checkFiveIsBuzz() {
		Assert.assertEquals("Buzz", funnyNumberFormatter.format(5));
	}

	@Test
	public void checkFourIsFour() {
		Assert.assertEquals("4", funnyNumberFormatter.format(4));
	}


	@Test
	public void checkBuzzNegativeNumber() {
		assertTrue(funnyNumberFormatter.isBuzz(-5));
	}
	
	@Test
	public void checkThirteenIsFormattedAsFizz(){
		Assert.assertEquals("Fizz",funnyNumberFormatter.format(13));
	}
	
	@Test
	public void fifteenIsFormattedAsFizzBuzz() {
		Assert.assertEquals("FizzBuzz", funnyNumberFormatter.format(15));
	}
	
}

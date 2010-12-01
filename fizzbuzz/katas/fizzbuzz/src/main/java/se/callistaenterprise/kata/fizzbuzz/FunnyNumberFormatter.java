package se.callistaenterprise.kata.fizzbuzz;

import java.util.ArrayList;
import java.util.List;

public class FunnyNumberFormatter {

	public List<String> format(List<Integer> numbers) {

		List<String> strings = new ArrayList<String>();
		for (int number : numbers) {
			strings.add(format(number));
		}
		return strings;
	}

	public String format(int number) {
		StringBuilder sb = new StringBuilder();
		if (isFizz(number)) {
			sb.append("Fizz");
		}
		if (isBuzz(number)) {
			sb.append("Buzz");
		}
		if (sb.length() == 0) {
			sb.append(Integer.toString(number));	
		}
		return sb.toString();
	}

	public boolean isFizz(int i) {
		return ((i % 3) == 0 || Integer.toString(i).contains("3"));
	}

	public boolean isBuzz(int i) {
		return (i % 5) == 0 || Integer.toString(i).contains("5");
	}

}

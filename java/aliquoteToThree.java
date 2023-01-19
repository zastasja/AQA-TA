import java.io.IOException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// 3. Составить алгоритм: на входе есть числовой массив, необходимо вывести элементы массива кратные 3

public class aliquoteToThree {
    public static void main(String[] args) throws IOException {
        System.out.println("Введите количество чисел:");
        Scanner q = new Scanner(System.in);
        int i = q.nextInt();
        System.out.println("Введите числа через пробел:");
        Scanner input = new Scanner(System.in);
        ArrayList<Double> nums = new ArrayList<Double>();
        do {
            nums.add(input.nextDouble());
            i--;
        } while (i > 0);
        System.out.println(nums);
        input.close();

        ArrayList<Double> l = new ArrayList<>();
        for (Double n : nums) {
            if (n % 3 == 0 && n != 0)
                l.add(n);
        }
        System.out.println("Числа кратные трем " + l);
    }

}
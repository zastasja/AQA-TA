import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
public class alg {
    //1. Составить алгоритм: если введенное число больше 7, то вывести “Привет”.

    public static void numberOverSeven(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        System.out.println("Введите число: ");
        double n = sc.nextDouble();

        if (n > 7) {
            System.out.println("Привет");
        }
        sc.close();
    }
//2. Составить алгоритм: если введенное имя совпадает с Вячеслав, то вывести “Привет, Вячеслав”,
// если нет, то вывести "Нет такого имени"
    public static void nameChecker(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Введите имя: ");
        String name = sc.nextLine();
        if (name == "Вячеслав"){
            System.out.println("Привет, " + name);
        } else {
            System.out.println("Нет такого имени");
        }
        sc.close();

    }


// 3. Составить алгоритм: на входе есть числовой массив, необходимо вывести элементы массива кратные 3
public static void aliquoteToThree(String[] args) throws IOException {
    System.out.println("Введите числа через пробел:");
    Scanner input = new Scanner(System.in);
    ArrayList<Double> nums = new ArrayList<>();
    System.out.println(nums);
    input.close();
    
}
    
}


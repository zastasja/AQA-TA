import java.io.IOException;
import java.util.InputMismatchException;
import java.util.Scanner;

 //1. Составить алгоритм: если введенное число больше 7, то вывести “Привет”.
public class numberOverSeven {

    public static void main(String[] args) throws IOException {
        try {
            Scanner sc = new Scanner(System.in);
            System.out.println("Введите число: ");
            double n = sc.nextDouble();

            if (n > 7) {
                System.out.println("Привет");
            }
            sc.close();
        } catch (InputMismatchException e){
            System.out.println("Неверный ввод");
        }

    }
}

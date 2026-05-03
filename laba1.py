class MatrixOperations:
    @staticmethod
    def execute():
        try:
            A = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]

            B = [
                [9, 8, 7],
                [6, 5, 4],
                [3, 2, 1]
            ]

            if len(A[0]) != len(B):
                raise ValueError("Неможливо перемножити матриці: кількість стовпців A не дорівнює кількості рядків B")

            rows_A = len(A)
            cols_B = len(B[0])
            C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

            for i in range(rows_A):
                for j in range(cols_B):
                    for k in range(len(B)):
                        C[i][j] += A[i][k] * B[k][j]

            print("Результат множення матриць (C = A * B):")
            for row in C:
                print(row)

            total = 0.0
            count = 0
            for row in C:
                for element in row:
                    total += element
                    count += 1

            if count == 0:
                raise ValueError("Матриця C порожня, неможливо обчислити середнє значення")

            average = total / count
            print(f"\nСереднє значення елементів матриці C: {average:.2f}")

        except ValueError as ve:
            print(f"Помилка значень: {ve}")
        except IndexError:
            print("Помилка індексу: перевірте розмірності матриць")
        except TypeError:
            print("Помилка типу: елементи матриць повинні бути числами")
        except ZeroDivisionError:
            print("Помилка ділення на нуль: неможливо обчислити середнє значення для порожньої матриці")
        except Exception as e:
            print(f"Невідома помилка: {e}")


if __name__ == "__main__":
    MatrixOperations.execute()
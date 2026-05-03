from typing import List


class Cosmetic:
    def __init__(self, name: str, brand: str, category: str,
                 price: float, volume_ml: int, rating: float) -> None:
        self.name = name
        self.brand = brand
        self.category = category
        self.price = price
        self.volume_ml = volume_ml
        self.rating = rating

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cosmetic):
            return NotImplemented
        return (self.name == other.name
                and self.brand == other.brand
                and self.category == other.category
                and self.price == other.price
                and self.volume_ml == other.volume_ml
                and self.rating == other.rating)

    def __repr__(self) -> str:
        return (f"Cosmetic(name={self.name!r}, brand={self.brand!r}, "
                f"category={self.category!r}, price={self.price}, "
                f"volume_ml={self.volume_ml}, rating={self.rating})")


class LabExecutor:
    @staticmethod
    def execute() -> None:
        try:
            cosmetics: List[Cosmetic] = [
                Cosmetic("Тональний крем", "LuxVisage", "декоративна", 450.0, 30, 4.3),
                Cosmetic("Зволожувальний крем", "AquaDerm", "доглядова", 320.0, 50, 4.8),
                Cosmetic("Туш для вій", "EyeArt", "декоративна", 280.0, 10, 4.0),
                Cosmetic("Сонцезахисний крем", "SunGuard", "доглядова", 500.0, 75, 4.5),
                Cosmetic("Помада", "ColorMe", "декоративна", 220.0, 4, 4.1),
                Cosmetic("Тонік для обличчя", "AquaDerm", "доглядова", 180.0, 200, 4.6),
            ]

            if not cosmetics:
                raise ValueError("Масив косметичних засобів порожній!")

            cosmetics.sort(key=lambda item: item.price)
            print("=== Масив, відсортований за ціною (зростання) ===")
            for product in cosmetics:
                print(product)

            cosmetics.sort(key=lambda item: item.rating, reverse=True)
            print("\n=== Масив, відсортований за рейтингом (спадання) ===")
            for product in cosmetics:
                print(product)

            search_target = Cosmetic(
                "Зволожувальний крем", "AquaDerm", "доглядова", 320.0, 50, 4.8
            )
            print(f"\n=== Пошук об'єкта: {search_target} ===")

            if search_target in cosmetics:
                print("Об'єкт знайдено в масиві.")
                index = cosmetics.index(search_target)
                print(f"Його індекс: {index}")
            else:
                print("Об'єкт НЕ знайдено в масиві.")

        except ValueError as ve:
            print(f"ValueError: {ve}")
        except AttributeError as ae:
            print(f"AttributeError: {ae}")
        except Exception as e:
            print(f"Непередбачена помилка: {e}")


if __name__ == "__main__":
    LabExecutor.execute()
class TextProcessor:
    @staticmethod
    def execute():
        try:
            text: str = (
                "The sun is bright today. "
                "The moon is bright at night. "
                "The stars shine bright in the sky. "
                "A cat sat on a mat. "
                "The cat is very cute. "
                "Dogs and cats are great pets. "
                "Bright colors make people happy."
            )

            if not text.strip():
                raise ValueError("Текст не може бути порожнім.")

            sentences: list[str] = []
            current_sentence: str = ""

            for ch in text:
                if ch in ".!?":
                    value: str = current_sentence.strip()
                    if value:
                        sentences.append(value)
                    current_sentence = ""
                else:
                    current_sentence += ch

            tail: str = current_sentence.strip()
            if tail:
                sentences.append(tail)

            if not sentences:
                raise ValueError("У тексті не знайдено жодного речення.")

            word_to_count: dict[str, int] = {}

            for sentence in sentences:
                words_in_sentence: set[str] = set()
                current_word: str = ""

                for ch in sentence.lower():
                    if ch.isalpha():
                        current_word += ch
                    else:
                        if current_word:
                            words_in_sentence.add(current_word)
                        current_word = ""

                if current_word:
                    words_in_sentence.add(current_word)

                for word in words_in_sentence:
                    word_to_count[word] = word_to_count.get(word, 0) + 1

            if not word_to_count:
                raise ValueError("У тексті не знайдено жодного слова.")

            max_count: int = max(word_to_count.values())
            max_words: list[str] = [
                w for w, count in word_to_count.items()
                if count == max_count
            ]

            print(f"Текст:\n{text}\n")
            print(f"Речення ({len(sentences)} шт.):")
            for index, sentence in enumerate(sentences, start=1):
                print(f"  {index}. {sentence}")

            print()
            print("Результат (C17=0):")
            print(f"  Найбільша кількість речень зі спільним словом: {max_count}")
            print(
                f"  Слів з такою частотою ({len(max_words)} шт.): "
                f"{', '.join(max_words)}"
            )

        except ValueError as ve:
            print(f"ValueError: {ve}")
        except AttributeError as ae:
            print(f"AttributeError: {ae}")
        except Exception as e:
            print(f"Непередбачена помилка: {e}")


if __name__ == "__main__":
    TextProcessor.execute()
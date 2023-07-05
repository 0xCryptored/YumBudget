from collections import Counter

def main():
    
    items = ['fried-egg', 'apple', 'blackberries', 'almond-milk', 'apple', 'apple', 'avocado']

    counter = Counter(items)

    synthesized_list = []

    for item, count in counter.items():
        if count > 1:
            synthesized_list.append(f"{count} {item}s")
        else:
            synthesized_list.append(item)

    print(synthesized_list)
main()

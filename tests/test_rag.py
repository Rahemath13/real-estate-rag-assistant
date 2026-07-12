from rag.chain import RealEstateRAG

bot = RealEstateRAG()

while True:

    question = input("\nYou : ")

    if question.lower() == "exit":
        break

    answer, sources = bot.ask(question)

    print("\nAssistant:\n")

    print(answer)

    print("\nSources:")

    for source in sources:
        print("-", source)
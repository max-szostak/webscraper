from shopping.shopping import Shopping

with Shopping() as bot:
    bot.land_first_page()
    bot.select_gender() # "Men" or "Women"
    bot.select_shoes()
    bot.sort_by_newest()
    bot.select_size(8) # 0.5 increments
    bot.refresh() # workaround to make results display in correct order
    bot.report_results()



class Library:
    def __init__(self, lib_id, meta, book_code, total_sc):
        self.lib_id = lib_id
        self.n_books = meta[0]
        self.n_sign_days = meta[1]
        self.books_per_day = meta[2]
        self.max_sc = total_sc
        self.book_id = book_code
        self.days_left = 0


files = ['a_example.txt', 'b_read_on.txt', 'c_incunabula.txt', 'd_tough_choices.txt',
         'e_so_many_books.txt', 'f_libraries_of_the_world.txt']

for file_name in files:
    data_file = open(file_name, 'r')
    n_books, n_lib, n_days = list(map(int, data_file.readline().split()))
    score_books = list(map(int, data_file.readline().split()))
    lib_data = []
    for lib_id in range(n_lib):
        lib_meta = list(map(int, data_file.readline().split()))
        lib_books = list(map(int, data_file.readline().split()))
        books_with_score = []
        for b_id in lib_books:
            books_with_score.append([b_id, score_books[b_id]])
        in_pair = sorted(books_with_score, key=lambda x: x[1], reverse=True)
        in_sc = sum([x[1] for x in in_pair])
        books = [x[0] for x in in_pair]
        lib_data.append(Library(lib_id, lib_meta, books, in_sc))
    data_file.close()

    sort_lib = sorted(lib_data, key=lambda x: (-1*(1/x.n_sign_days)*x.n_books*x.max_sc*x.books_per_day))

    days_left = n_days
    to_execute = []
    for lib in sort_lib:

        if (days_left - lib.n_sign_days > 0) and (len(lib.book_id) > 0):
            lib.days_left = days_left - lib.n_sign_days
            days_left -= lib.n_sign_days

            to_execute.append(lib)
        else:
            break

    books_queue = []
    for lib in sort_lib:
        in_books = lib.book_id.copy()
        selected_books = []
        left_books = []
        acc_books = lib.days_left*lib.books_per_day
        while in_books and acc_books:
            first = in_books.pop(0)
            if first not in books_queue:
                books_queue.append(first)
                selected_books.append(first)
                acc_books -= 1
            else:
                left_books.append(first)
        selected_books.extend(in_books+left_books)

        lib.book_id = selected_books.copy()

    out_str = ''
    out_str += str(len(to_execute)) + '\n'
    for lib in to_execute:
        out_lib_id = lib.lib_id
        out_n_book = lib.days_left * lib.books_per_day
        if out_n_book > lib.n_books:
            out_n_book = lib.n_books
        out_str += str(out_lib_id) + ' ' + str(out_n_book) + '\n'
        out_books_arr = lib.book_id[:out_n_book]
        for x in out_books_arr:
            out_str += str(x) + ' '
        out_str += '\n'

    with open('out_'+file_name, 'w') as out_file:
        out_file.write(out_str)

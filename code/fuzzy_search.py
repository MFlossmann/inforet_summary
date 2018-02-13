def process_fuzzy_query(x, q, delta, q_gram_index):
    x_q_grams = pad(x, q)  # pad the query string
    doc_id_list = []
    for q_gram in x_q_grams:
        lst = q_gram_index.fetch(q_gram)
        doc_id_list = merge_and_count(doc_id_list, lst)

    # now, doc_id_list contains all words with common q-grams, as well as how
    # many they have in common

    for id in doc_id_list:
        minimum_in_common = max(len(x), len(y)) - 1 - (delta - 1) * q
        if id.amount_in_common >= minimum_in_common:
            edit_distance(id.word, x)  # now, we should compute the actual edit
            # distance
        else:
            pass  # discard this entry with too little in common


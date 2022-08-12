import csv
import gensim.downloader as api
import sys

def fetch_synonyms(words, file_name, pretrained_model) :
    try:
        model = model = api.load(pretrained_model)   
    except ValueError:
        sys.exit(f"** Error: gensim model {pretrained_model} does not exist")
    except:
        sys.exit(f"** Error: gensim model {pretrained_model} could not be loaded")


    similarities = []
    for word in words:
        try:
            similar = model.most_similar(word, topn=3)
        except Exception:
            similar = [("", 0)]

        similar_str = "\t".join([(w[0]) for w in similar])
        similarities.append((similar[0][1], word, similar_str))

    similarities.sort(key=lambda x: x[0], reverse=True)

    with open("generated_synonyms.csv", 'w') as fp:
        csv_writer = csv.writer(fp, delimiter=',', quotechar='"')
        for i in similarities:
            csv_writer.writerow([i[1]] + ['/'.join(i[2].split('\t'))])

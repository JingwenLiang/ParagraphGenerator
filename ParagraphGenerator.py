import re
import random

class ParagraphGenerator():
    def __init__(self, args):
        self.dataset = args.dataset
        self.P = args.P
        self.N = args.N
        self.CUTOFF = 100
        self.prefix_cnt = 0
        self.word_dic = {'<BOS>':[]}

    def vocab(self):
        """Create the vocabulary from the input paragraphs.
        Each paragraph is prefixed with a <BOS> token, and subfixed with
        a <EOS> token. The vocabulary is a dictionary with keys to be possible
        prefix, and values to be a candidate list of possible next words.
        There are duplicates in the candidate list according to the frequency
        of words in the input paragraphs.
        """
        with open(self.dataset,'r') as f:
            for i, line in enumerate(f):
                line_list = ['<BOS>'] + re.findall(r"[\w']+|[.,!?;]", line) + ['<EOS>']
                if len(line_list) <= 2:
                    continue
                j = 0
                self.word_dic['<BOS>'].append(line_list[1])
                while j+self.P < len(line_list):
                    prefix = ''.join(line_list[j:j+self.P])
                    if prefix in self.word_dic:
                        self.word_dic[prefix].append(line_list[j+self.P])
                    else:
                        if j > 0 and j+self.P < len(line_list)-1:
                            self.prefix_cnt += 1
                        self.word_dic[prefix] = [line_list[j+self.P]]
                    j+=1

    def join_punctuation(self, seq, characters='.,;?!'):
        """Join a list of words and punctuations with punctuations in the
        right places.

        @type  seq: list
        @param seq: list of words and punctuations
        @return: list of words with punctuations appended to the right position
        """
        characters = set(characters)
        seq = iter(seq)
        current = next(seq)
        for nxt in seq:
            if nxt in characters:
                current += nxt
            else:
                yield current
                current = nxt
        yield current

    def generate(self):
        """Generate paragraphs according to the created vocabulary dictionary.
        The generation will terminate whenever the length of the generated paragraph
        is longer than the curoff length (100), or the ending token <EOS> appears.

        @return: a list of generated sentences, the unique prefix count
        """
        self.vocab()
        n = 1
        output = []
        while n <= self.N:
            cur = '<BOS>'
            generated_sen = ['<BOS>']
            count = 0
            while True:
                count += 1
                try:
                    candidate = self.word_dic[cur]
                except:
                    print("Input P is too large!")
                    break
                next = random.choice(candidate)
                generated_sen.append(next)
                cur = ''.join(generated_sen[-2:])
                if next == '<EOS>' or count >= self.CUTOFF:
                    break
            n += 1
            output.append(' '.join(self.join_punctuation(generated_sen[1:-1])))

        return output, self.prefix_cnt

from collections import defaultdict



input = "dcbcsbblhhgdgssmcmqccdwdvwdvvcfvcfvvpvmmwccdqddshhdppcfpfbbfggfjfvvhzhmmsqswsttcgtctggjllhnnqbnnnldlglplvlbvbzztpzzvpphshwwfhhgssvgsvvpfvfzznbznndqqtsqttnvtvqqqrgqrrgzzlqzzbvzbzmzffnbfnbffcggdcggqhqpqzpqzqbbqvbqbhhtzhhrrrprlrclrcrssqspqpbblggfvvbpvbbssvttsztzpzjjwffnpnfnrrqhqgqrrzqzbzzdpdjpplpclpptltztjtztqthtmmmpsmmpjpqpvvshhsfshhrvrdvdggwssdbbzbttlmlmpprmrmlrrmqrqsshjhjljzjnjllbbvjvnnppqbppqqfffrbfbdfbbqppmtppfttqddtzzwbblqqbddgwgqwqzwwpzwzjjbccdjdwwrggrmrtmrtmrrvpptwwcdcwwsdshhjjhwjwqjwwqsshrrbsblssphspsjpssnsmsqswqwfwjwccdvccrqqnsqnsnwsnsmnmccvcqqfjjfljfljfjgjffjvffvjvhjhfhrfrlrrtpphbhwbbvmmnpndnlljdjfjsffvccnhchwhddrccljllmnnhmnmpnnhtnthnhvnhnwnqqjmmgzzvssphhjljbjwjbwwdnwwdvvzpvvhccvjjlclrrppgjgsshghvvzjvvpvvbjjqhjqqfcqffchcmmvdvtddftdtppfnppcnpnznwwpdpjpnpttlbbmmqfqmffqnfnbffbrbgbwggsmsbbfgbbfbzbtzbbvmmdlmlrlnlwwbswsjjpjhhwqwzqznqzqvvwccwvwwcbbpvvwcvcvzzhzchzccbnccjlljsjbjdbbvqbvvfdfgdfggzfzlzmzrznnqsnncmnnljjtcjcfftrthtrhrgrvvjggzpggrcrpcppggdfggpmmwnmnlmlglvvmjvvddsmsjsnjssqffffctczcjzjjlbbhpbbfdbdzbbsjbjnjbbqqjbqjbjjhwhssmvsschhhwppbjppllprpjrppdpfpgpjptjtptplpnptnptpjjmcmnnnhnjhjlhjlhjlhlwwhwmwjjbhhlfffrbbgvvqwvwswtstmmmfpmfpffmcfcrrqsqzqjjjnpnnztnznddlwdldsdbssstzstswwjtttmmwmsmwssvswszsjzsjjsffmccmfccqzzvpmbbbsqffgzdqbjtzhlqdzhlpwghlstcrcrffrnbwjnqgmbmpgttfmsswdqctlrpdnlsgnlldvbfpwtcptvbwftzcnbbscrrcpnwtmllcvsrmwzzlsdmfctdcwsqdlsnzgfpmzrnswhbqjhstztzzmzpcttsgsggnlhvjmcbbrhgqhsfmglpcbdvmmmnfbtbfrqbpcmttjtnwvznbshwrmznnsvpjqjntlzspljnbwtjcqztsfcqlrggrpzjgjsvqqcrmrjmzwdsshqfhbtfmlwmfvtbcgdmjgtcnphfmfmjlbjzrvjslccftnwcchgdwjnlthlwgldjwqwgdptdjdmzdrrzcdpbfrtdgcspjtqdqvzswwdwrhggdrqjjgwwrbwhhlrpqmszvlvjfqptncjlscvzbgzgmsttlbhbfrctnsphjcrcwlhcgrcrsjbrjvptgfbjgjrvtzmnhpzcgptbmrgvstsltnctjphsjdwpdqblfswzfhgjbpfrptlmhfwcpdlzqccgtdvbzhwngrhlqftmlhjprscflgzpflvvpfsjmlnmbzsrlrshvnsqrhhlqdlzhrcbjjjfrbqcdspwsmltcrtlbdnbnvhbbwgqdcncsztbfwztzdbqgcrnvndmpstpncbwvtctzdpmcpvrgqvjjztfwpvjtdqlvcvdpfzgcghsmbcwtzztmqwdpsprgsmfhphqsqmflrjdqzjscgzlnvcwcrlmpdscnhqpqjfdbdftqgttwntdbpnshdwnmwsrslfgnzlnwwwqgdbfnthhqtvbzsqgzjhhghtmvvfhlmlpbghnsvlttzsjlgndhdqmqqfdlqnbfscsnnqzcdwzdlqcnstcbsffghftqvwrsshgwmlnprhdnnwslwfwtmtfzdjwpmlvvdhjvdwrhvdsmpgrdpnqsjpqmhttrmdwllrmnbznwjwvvpjnnbnfzbdnhjbqqrnzgdqbspbqtwdpgsbwpzfdbpvzfjpsgmztnzrpvvhwlfscfvfpfblvplgdbhvjjpdjtnwrmvpjsphvglpsntvwtqwqvprcgwjltddpjngvmzfzhmqnnwglbzsbrcztpplpsmgmcfgzgpbtgsjrfvdzzcsthznvdpbwvdlcgdhncsjdvpcbbmtrqczctjljdfghsrvrsfjglqqhjttfdhqdqwhzhqrggsjwlldrntwmmbftgqjhpvvctpbtgltnttlhdqbsbwcqmctwlsnhmhncpmnzsllmjhcgnlfgvpcqrwzvsstgwbvjtnrlbblclzdrcwddrwnptqzgwdwtgrfwffpzjmwbqfmmrcfzfzjbwsslbhggtwtcrlhffzgfgrtljgnznnlgzwfmtwwqzhlthvpfclrtmrqfzrggbctzfsmjhrtwzpfrnhwwprnbwmvwvmvnzqpggmzgslctqbqdtvhgzjwzsnblqzmcpnpwllzhvzzmfqzfjlrsrcnjzqdzbpjftljtzvvmrjszvqllnhhgnrnqttnwlvllphjtnmlwqhcvmbsvnwtcdmhsmhdcwqwtvggcqfpdsrsscmhcvfzvdnffrfhdfmgbsghdbpwdwrdmlvsnzwcfchcqvccszdqrbnfvrpbftcwnjmczwgqzmtlmrthlhtjpmchltcmcqwgfgshtvtpmcmpbmlnjmhnpdsljjmjzddnlgtnjqztzsqqlhtqcscjvjncjvfcvsgjhqgzrmtjjcgvvmwswffmlcvlhqhbvrldrvbrfmmqcnqmfzlsghvclrdbsvcbqspgbzmjnlrdhvncnbcfmdlqrssggsmlwwglcjjzmcdwcnrgvvmgjcfbzlncmgqtllgldbdztbtfcjczqtjjlnpqmrgtjsmrbscvqlgqghfbgwccgwrjrzrsbbrqnjcqhllsqmrjtzmjnndwwmdjfhspjpgdcjjpdvwrsgjcfnpllnnnccvnfvqbpddgvbgbsbczmbzrbclczljdmbhpgmhwlqvnjzjwzzfjmsmcchjrqrtmhwlgjsptctlbtdnrqgntcvngcrqdqptfmhbvlhrqchdtwdwbrbqwtswzcrrfndldwmjbczppzrnncvvqsmpvvqcnsvhprhlmrhnjbwdvrbbwwdtmzrqttschrztgjcshlhfbmhmwrrmwgmfshpdhjwgdmcfdvqrmmwgmzbrlgbfltvlzmvqbgvhppdzglqbdlrhjnntnfvtmzjqccmqdbpjqphfggmjqdrndhclcfvqsjrsbcgdhcrbjsdjmwrzvpfpcjwjfdltztfzgmlzqzmztpvbflppgnhdzssznngfjggczdtdmcczjzfsnflpwqrbggmqdbbprfptzcdqvhrvszzjqqjlrlrdpwcnzhvgfhpcdbbgsfmtnszwbhwcdwdghqqctwqlqrlqbdwfvjnhcpmzchqfrwzhzgslzhncmrlrpzcjczvzwcvwcldbmscfqnnqnwwvrpfvjswqmhgmhgnmfzpsjmdhbpvsftccttvdpcdzcnzswqmtrwbctpbgmzrvrrshjjgdqsqrwfpcmsbvqhccvjqpztlttwjjdtbmwslschpqjjllvjcjwtmrtvvwdzglstvtpndmmzcpgqsvqgfdtqdjdctsbsbmqzqhtczhgqgwbdlrhjrwcmtbzfndsbnpnhmsdhtghwwzvtdwtscdnwzmrjrsrjvvbvrpbszchwbltrjbcqmlhqnzcfbhjqnsjghlnlbsrgzrrzfvslwpbqmgfswhgjdsdfrzsdhvdqvqfbcbvmbfhjfpzwlbspcbnvrgpfnmjbwbsnpqpqhjpsnwrlcmfhpdmjbvpnctcfqgdmwzblsnr"
# input = "nppdvjthqldpwncqszvftbrmjlhg"

last_char_group = input[:14]
print(last_char_group)

r_idx = 14
l_idx = 0
while len(set(last_char_group)) != 14: 
    l_idx += 1 
    r_idx += 1 
    last_char_group = input[l_idx:r_idx]
    
    
print(last_char_group)
print(r_idx)
def string_to_words(filepath):
    with open(filepath) as f:
        text = f.read()
        count = 0
        words = text.split()
        for word in words:
          count += 1
    return count 

def char_count(filepath):
   with open(filepath) as f:
      text = f.read()
      text = text.lower()
      char_count = {}
      for char in text:
         if char in char_count:
            char_count[char] += 1
         else:
            char_count[char] = 1
   return char_count       

def sort_on(dict):
    return dict["count"]


def sort_char(char_dict):
   sorted_list = []
   for char in char_dict:
      if char.isalpha():
         sorted_list.append({'char': char, 'count': char_dict[char]})
   sorted_list.sort(key=sort_on, reverse=True)
   return sorted_list
     

            
   

def recommand_id(new_id):

    new_id=new_id.lower()
    allowed_word = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','s','t','u','w','x','y','z',
                    '0','1','2','3','4','5','6','7','8','9', '-', '_', '.']
    for word in new_id:
        if word not in allowed_word:
            new_id = new_id.replace(word, '')

    while '..' in new_id:  #해답 참조
        new_id=new_id.replace('..','.')

    if new_id[0] == '.':
        if len(new_id)>1:
            new_id=new_id[1:]
        else:
            new_id='.'
    if new_id[-1]=='.':
        new_id=new_id[:-1]

    if len(new_id)==0:
        new_id='a'
    elif len(new_id)>=16:
        new_id=new_id[:15]
        if new_id[-1]=='.':
            new_id=new_id.replace(new_id[-1],'')
    if len(new_id)<=2:
        while len(new_id)<3:
            new_id+=new_id[-1]
            
    return new_id

new_id=input()
answer=recommand_id(new_id)

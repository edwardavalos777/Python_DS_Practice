def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # Split the phrase into a list of words
    words = phrase.split()
    
    #capitalize the first lettr of each word
    capitalized_words = [word.capialize() for word in words]

    #join the capitalized words into a new string 
    return ' '.join(capitalized_words)

    

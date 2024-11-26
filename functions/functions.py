def p_value_to_words(p_value):
    if p_value < 0.001:
        print("*** Very Significant! p < 0.001 ***")
    elif p_value < 0.05:
        print("** Significant! p < 0.05 **")
    else:
        print("Not significant. p = {:.3f}".format(p_value))
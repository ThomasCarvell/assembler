loop    LDA num1
        STA temp
        ADD num2
        STA num1
        LDA temp
        STA num2
        LDA inst
        ADD one
        STA inst
        LDA num1
inst    STA temp
        BRA loop
num1    DAT 1
num2    DAT 1
temp    DAT 0
one     DAT 1
/**
 * Created by Lexi on 12/29/2016.
 */

var turn = false;
var win = false;



function winCheck() {
    var TL = $('#one').html();
    var TM = $('#two').html();
    var TR = $('#three').html();
    var ML = $('#four').html();
    var MM = $('#five').html();
    var MR = $('#six').html();
    var BL = $('#seven').html();
    var BM = $('#eight').html();
    var BR = $('#nine').html();

    if (TL == TM && TM == TR && TM != '<p>*</p>') {
        win = true;
        console.log('top row win')

    } else if (ML == MM && MM == MR && MM != '<p>*</p>') {
        win = true;
        console.log('middle row win');

    } else if (BL == BM && BM == BR && BM != '<p>*</p>') {
        win = true;
        console.log('bottom row win')

    } else if (TL == ML && ML == BL && ML != '<p>*</p>') {
        win = true;
        console.log('left column win')

    } else if (TM == MM && MM == BM && MM != '<p>*</p>') {
        win = true;
        console.log('middle column win')

    } else if (TR == MR && MR == BR && MR != '<p>*</p>') {
        win = true;
        console.log('right column win')

    } else if (TL == MM && MM == BR && MM != '<p>*</p>') {
        win = true;
        console.log('Top left to bottom right diagonal win')

    } else if (BL == MM && MM == TR && MM != '<p>*</p>') {
        win = true;
        console.log('Bottom left to top right diagonal win')
    }

}

//            So this is the game logic section
//        if you click on a .square
    $('.square').click(function() {
//                if the square chosen is equal to <p>*</p>, then play on
//                else keep on choosing
        if ($(this).html() == '<p>*</p>') {
//                if playable, then convert the .html() of chosen .square and change it to x
        if (turn == false) {
            $(this).html('x').css('font-size', '150px');
//                    make turn = true to allow next player to play
            turn = true;
//                    this message is a guide for who's turn it is
            $('#message').html('Player 2 turn');
//                    winCheck() in order to see if anyone has won yet
            winCheck();
//                    if win == true display the win message
            if (win == true) {
                $('#message').html('Player 1 (x), wins!');
                console.log('x wins');

            }

//                    Same sort of stuff os the block above, except for 'o' player
        } else if (turn == true) {
            $(this).html('o').css('font-size', '150px');
            turn = false;
             $('#message').html('Player 1 turn');
             winCheck();
             if (win == true) {
                 $('#message').html('Player 2 (o), wins!');
                 console.log('o wins')
             }
        }
    }
        });

$('#chosenOne').click(function() {
    var TL = $('#one').html();
    var TM = $('#two').html();
    var TR = $('#three').html();

    console.log(TL, TM, TR);
})


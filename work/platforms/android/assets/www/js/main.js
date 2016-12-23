
document.addEventListener("deviceready", onDeviceReady, false);



//global variables

var db;
var q =  '"' ;
var bt = ' between ';
var equals = '=' ;
var from =  '>=';
var upto =  '<=';
var and = ' and ';
var or = ' or ';
var ch = 'Chapter';
var vr =  'Verse' ;
var op = ' (' ;
var cp =  ') ' ;
var base = 'select * from Content where Book=';

function onDeviceReady() {
    db = window.sqlitePlugin.openDatabase({name: "bible.db", location: 'default', createFromLocation: 1});
    window.open = cordova.InAppBrowser.open;
    dbMaint();
}

//  datebox issues

function dbMaint(){
    
    $('.form-control').attr('readonly', true); // disable keyboard input
}


function yayB(day){
    db.transaction(function (tx) {
        tx.executeSql('select * from Readings where Date ='+ "'" +day+ "'" , [], getReadings, errorCB);
      })
}

function errorCB(err) {
    alert( "Error processing SQL:"  +err.code);
}


function getReadings(tx, results) {
    var items = results.rows.item(0);
    var columns = {FirstReading : 'First Reading', Psalm : 'Psalm', SecondReading : 'Second Reading', Acclamation: 'Acclamation', Gospel:'Gospel'};
    var day = items.Day
    var textDay= '<h2 id= day >' + day + '</p> <h2 id= title ></h2><div id= readings ></div>  <h2 id= title ></h2><div id= readings ></div>  <h2 id= title ></h2><div id= readings ></div> <h2 id= title ></h2><div id= readings ></div> <h2 id= title ></h2><div id= readings></div>' ;                             //day title
    document.getElementById("deviceready").innerHTML = textDay;
    for(key in columns){
        if (items[key]){                                                   //readings loop
            var reading = items[key];
            var readingID = key;
            var readingTitle = columns[key];
            var bookname = reading.match(/(\d )?[A-z]+/)[0];
            var book = getBookNb(bookname);
            var unclean_chapters = reading.match(/\d+:/g);
            var chapters = clean(unclean_chapters);
            var b = reading.split(':');
            var sqlselect = base + book + and;                     //select book
            for(var i=1; i < b.length; i++){                               //chapters loop
                var chapter = chapters[i-1];
                if (i != 1){
                    sqlselect += or;
                }
                sqlselect += op + ch + equals + chapter + and + op;//select chapter
                var sp = b[i].split(',');
                var dd; //double-dash
                for (v in sp){
                    var verse = sp[v].match(/\d+(-\d+)?/)[0];              //verses loop
                    if (v != 0){
                        sqlselect += or;
                    }
                    if (dd === true){
                        dd = false;// unset dd
                        sqlselect += op + vr + upto + verse + cp;     //select verse before double-dash w/pattern (Nb--)
                        continue;
                    }
                    if (sp[v].indexOf('--') !== -1){
                        dd = true;// set dd for next verse upto (--verse)
                        sqlselect += op + vr + from + verse + cp;     //select verse after double-dash w/pattern (--Nb)
                        continue;
                    }
                    if (sp[v].indexOf('-') !== -1){
                        var vs = verse.split('-');
                        sqlselect += op + vr + bt + vs[0] + and + vs[1] + cp;//select verses between w/pattern (Nb-Nb)
                        continue;
                    }
                    sqlselect += op + vr + equals + verse + cp;                   //select single verse (Nb,)
                }
                sqlselect += cp + cp;

            }
            tx.executeSql(sqlselect, [], function(tx, results) {   // get readings  from database
                        var text ='<div class= outer >';
                        var len = results.rows.length;
                        for (var i = 0; i < len; i++) {
                        text +=
                        '<div class= chunk >'+
                        '<div class= foreign >'+
                        results.rows.item(i).Original +
                        '</div>'+
                        '<div class= translation >'+
                        results.rows.item(i).Translation +
                        '</div>'+
                        '<div class= pronunciation >'+
                        results.rows.item(i).Pronunciation +
                        '</div>'+
                        '</div>';
                        var book = results.rows.item(i).Book;
                        }
                        text += '</div>' ;

                         if (book<=39){
                          document.getElementById("readings").dir ="rtl";
                          $("#readings:first").addClass("hebrew");    
                          }
                        else{
                            $("#readings:first").addClass("greek");
                        }
                        document.getElementById("readings").innerHTML = text;
                        document.getElementById("readings").id = "reading";
                    }, errorCB);
            document.getElementById("title").innerHTML = readingTitle + " (" + reading +  ")" ;
            document.getElementById("title").id =  readingID;
        }
    }
}


function clean(unclean) { //helper function to clean spaces and colons
    var cleaned = [];
    for (item in unclean){
        cleaned.push(unclean[item].replace(/\s|:/g,""));
    }
    return cleaned;
}


function getBookNb(key){  //helper function to get bookname
    var booknames = {
        'Genesis':1,
        'Exodus':2,
        'Leviticus':3,
        'Numbers':4,
        'Deuteronomy':5,
        'Joshua':6,
        'Judges':7,
        'Ruth':8,
        '1 Samuel':9,
        '2 Samuel':10,
        '1 Kings':11,
        '2 Kings':12,
        '1 Chronicles':13,
        '2 Chronicles':14,
        'Ezra':15,
        'Nehemiah':16,
        'Esther':17,
        'Job':18,
        'Psalms':19,
        'Proverbs':20,
        'Ecclesiastes':21,
        'Solomon':22,
        'Isaiah':23,
        'Jeremiah':24,
        'Lamentations':25,
        'Ezekiel':26,
        'Daniel':27,
        'Hosea':28,
        'Joel':29,
        'Amos':30,
        'Obadiah':31,
        'Jonah':32,
        'Micah':33,
        'Nahum':34,
        'Habakkuk':35,
        'Zephaniah':36,
        'Haggai':37,
        'Zechariah':38,
        'Malachi':39,
        'Matthew':40,
        'Mark':41,
        'Luke':42,
        'John':43,
        'Acts':44,
        'Romans':45,
        '1 Corinthians':46,
        '2 Corinthians':47,
        'Galatians':48,
        'Ephesians':49,
        'Philippians':50,
        'Colossians':51,
        '1 Thessalonians':52,
        '2 Thessalonians':53,
        '1 Timothy':54,
        '2 Timothy':55,
        'Titus':56,
        'Philemon':57,
        'Hebrews':58,
        'James':59,
        '1 Peter':60,
        '2 Peter':61,
        '1 John':62,
        '2 John':63,
        '3 John':64,
        'Jude':65,
        'Revelation':66,
        'Judith':67,
        'Tobit':68,
        '1 Maccabees':69,
        '2 Maccabees':70,
        '3 Maccabees':71,
        '4 Maccabees':72,
        'Wisdom':73,
        'Baruch':74,
        'Sirach':75,

    };

    return booknames[key];
}

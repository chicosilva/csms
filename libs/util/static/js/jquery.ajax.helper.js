try{var $xi = Dajaxice, $x = Dajax;}catch(e){}
$('.cepfill, .controls #id_cep, #id_cep').blur(function () {
    var $o = $(this);
    if ($o.val() != undefined && $o.val() != null && $o.val() && $o.val().indexOf('_') < 0) {
        var $anterior = $o.attr('rel');
        if($anterior != $o.val()){
            try {
                wait('Consultando os correios, por favor aguarde.');
            } catch (e) {
            }
            $o.attr('rel', $o.val());
            $xi.libs.util.cep($x.process, {cep: $o.val(), cepid: $o.attr('id')});
        }
    }
});

(function($) { $.fn.blink = function(options) { var defaults = { highlightClass: "highlight", blinkCount: 3, fadeDownSpeed: "slow", fadeUpSpeed: "fast", fadeToOpacity: 0.33 }; var options = $.extend(defaults, options); return this.each(function() { var obj = $(this); var blinkCount = 0; obj.addClass(options.highlightClass); doBlink(); function doBlink() { if (blinkCount < options.blinkCount) { obj.fadeTo(options.fadeDownSpeed, options.fadeToOpacity, function() { obj.fadeTo(options.fadeUpSpeed, 1.0, doBlink); }); } else { obj.removeClass(options.highlightClass); } blinkCount++; } }); }; })(jQuery);

$('.masked').each(function () { $(this).mask($(this).attr('mask')); });

Number.prototype.formatMoney = function (c, d, t) {
    var n = this, c = isNaN(c = Math.abs(c)) ? 2 : c, d = d == undefined ? "," : d, t = t == undefined ? "." : t, s = n < 0 ? "-" : "",
        i = parseInt(n = Math.abs(+n || 0).toFixed(c)) + "", j = (j = i.length) > 3 ? j % 3 : 0;
    return s + (j ? i.substr(0, j) + t : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + t)
        + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : "");
};

function confirmar(msg, yes, no) {
    var $var = $('#confirmdlg');
    $var.find('#dlgmsg').html(msg);
    $('#cdlgyes').click(function () {
        $.unblockUI();
        yes();
    });
    $('#cdlgno').click(function () {
        $.unblockUI();
        no();
    });
    $.blockUI({ message: $var });
}

function wait(msg, timeout) {
    if (!timeout) {
        timeout = 10000;
    }
    if (msg==null || msg==undefined || msg==''){
        msg = 'Carregando...';
    }
    $.blockUI({
        message: '<table style="width:100%;"><tr><td width="3"><div id="circularG"><div id="circularG_1" class="circularG"></div><div id="circularG_2" class="circularG"></div><div id="circularG_3" class="circularG"></div><div id="circularG_4" class="circularG"></div><div id="circularG_5" class="circularG"></div><div id="circularG_6" class="circularG"></div><div id="circularG_7" class="circularG"></div><div id="circularG_8" class="circularG"></div></div></td><td><h3 style="text-align:center; width:100%; color:#FFF;">' + msg + '</h3></td></tr></table>',
        timeout: timeout,
        css: {
            fontSize: '14px',
            border: 'none',
            padding: '15px',
            backgroundColor: '#FB607A',
            '-webkit-border-radius': '10px',
            '-moz-border-radius': '10px',
            opacity: .5,
            color: '#fff'
        }
    });
}

function loading(msg) {
    if (msg == null || msg == undefined || msg == '') {
        msg = 'Carregando...';
    }
    $.blockUI({
        message: '<table style="width:100%;"><tr><td width="3"><div id="circularG"><div id="circularG_1" class="circularG"></div><div id="circularG_2" class="circularG"></div><div id="circularG_3" class="circularG"></div><div id="circularG_4" class="circularG"></div><div id="circularG_5" class="circularG"></div><div id="circularG_6" class="circularG"></div><div id="circularG_7" class="circularG"></div><div id="circularG_8" class="circularG"></div></div></td><td><h3 style="text-align:center; width:100%; color:#FFF;">' + msg + '</h3></td></tr></table>',
        css: {
            fontSize: '14px',
            border: 'none',
            padding: '15px',
            backgroundColor: '#FB607A',
            '-webkit-border-radius': '10px',
            '-moz-border-radius': '10px',
            opacity: .8,
            color: '#fff'
        }
    });
}

$('a.blockui, input[type=submit].blockui').click(function () { wait() });

function dmsg(o) {
    msg(o.a, o.b);
}
function msg(txt, tipo) {
    var border = '#000000';
    if (tipo == 'success') {
        txt = '<div class="bluimg msg"><img src="' + STATIC_URL + 'images/success48.png" width="48" height="48" />' + txt + '</div>';
        border = ' #07BE55';
    }
    else if (tipo == 'info') {
        txt = '<div class="bluimg msg"><img src="' + STATIC_URL + 'images/info48.png" width="48" height="48" style="margin-top:5px;" />' + txt + '</div>';
        border = ' #173FB4';
    }
    else if (tipo == 'error') {
        txt = '<div class="bluimg msg"><img src="' + STATIC_URL + 'images/error48.png" width="48" height="48" style="margin-top:5px;" />' + txt + '</div>';
        border = ' #F6330E';
    }
    else if (tipo == 'warning') {
        txt = '<div class="bluimg msg"><img src="' + STATIC_URL + 'images/warning48.png" width="48" height="48" style="margin-top:5px;" /><h1>' + txt + '</h1></div>';
        border = ' #FA920C';
    }
    $.blockUI({
        message: txt,
        fadeIn: 700,
        fadeOut: 700,
        timeout: 2288,
        showOverlay: true,
        centerY: true,
        css: {
            width: '35%',
            top: '25%',
            minHeight: '32px',
            right: '10px',
            border: '2px solid' + border,
            padding: '15px',
            backgroundColor: '#fff',
            '-webkit-border-radius': '10px',
            '-moz-border-radius': '10px',
            'border-radius': '10px',
            color: border
        }
    });
}

$(".frmns").submit(function (e) {
    return false;
});

function newPopup(url) {
	popupWindow = window.open(url,'popUpWindow','height=600,width=800,left=10,top=10,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes')
}

// Messages --------------------------------------------------------------------------------------------------------- //
var myMessages = ['info','warning','error','success'];
function hideAllMessages() {
    var messagesHeights = [];
    for (i = 0; i < myMessages.length; i++) {
        var $container = $('.' + myMessages[i]);
        messagesHeights[i] = $container.outerHeight();
        $container.css('top', -messagesHeights[i]);
        $container.find('h3').html('');
        $container.find('p').html('');
    }
}
function showMessage(type, text, title) {
    hideAllMessages();
    var $container = $('.message.' + type);
    $container.addClass('msgready');
    if (title){ $container.find('h3').html(title); } else { $container.find('h3').remove(); }
    $container.find('p').html(text);
    $('.msgready.' + type).animate({top: "0"}, 500);
    $container.removeClass('msgready');
    setTimeout(function() { $container.trigger('click') }, 6000);
}


function babycrawling(){
    $('.babycrawling').show();
}

// Autoload --------------------------------------------------------------------------------------------------------- //
$(function () {
    $(document).on('ajaxStart',function () {
        wait();
    }).on('ajaxStop', function () {
        $.unblockUI();
    });
    hideAllMessages();
    $('.message').click(function () {
        $(this).animate({top: -$(this).outerHeight()}, 500);
    });
});

// ------------------------------------------------------------------------------------------------------------------ //
function cadnews(btn){
    var $frm = $(btn).parent('form');
    $xi.website.cadastra_news($x.process, {nome: $frm.find('input[name=nome]').val(), email: $frm.find('input[name=email]').val()});
    return false;
}

$('.barra-chat').click(function () { $(this).hide(); });
//$("a[rel*=mdl]").leanModal({ zIndex: 999, overlay: 0.4, closeButton: ".modal_close" });

$('#sbmtlgn').click(function () {
    var $email = $('input[name=lgnemail]');
    var $senha = $('input[name=lgnsenha]');
    var token = $('input[name=csrfmiddlewaretoken]').val();
    var next = $('input[name=lgnnext]').val();
    if (!$email.val() || $email.val() == undefined || $email.val() == null || $email.val() == '') {
        $email.css({border: '1px solid red'});
        showMessage('error', "Insira um e-mail válido", "Atenção");
    } else {
        $email.css({border: '1px #c6c6c6 solid'});
        if (!$senha.val() || $email.val() == undefined || $email.val() == null || $email.val() == '') {
            $senha.css({border: '1px solid red'});
            showMessage('error', "Digite sua senha", "Atenção");
        }
        else {
            $senha.css({border: '1px #c6c6c6 solid'});
            wait('Aguarde! Estamos validando os dados informados...');
            $xi.cliente.autenticar($x.process, {e: $email.val(), s: $senha.val(), t: token, n: next});
        }
    }
    return false;
});
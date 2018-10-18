(function() {
    'use strict';

    let $blocks = document.querySelectorAll('.{css_class}');
    $blocks.forEach(function($oneBlock) {
        $oneBlock.innerHTML = window.atob(
            localStorage.getItem(
                $oneBlock.getAttribute('id')));
    });
})();

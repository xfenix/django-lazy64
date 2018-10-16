(function() {
    'use strict';

    let $blocks = document.querySelectorAll('.CSS_CLASS');
    $blocks.forEach(function($oneBlock) {
        $oneBlock.innerHTML = window.atob(
            localStorage.getItem(
                $oneBlock.getAttribute('id')));
    });
})();

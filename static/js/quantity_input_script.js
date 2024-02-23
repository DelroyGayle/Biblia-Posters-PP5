/*jshint esversion: 11 */

/*
    In light of a bug that I discovered in the Shopping Bag Refactor approach 
    regarding the Walkthrough
    I have amended the original 'handleEnableDisable(itemId)' function
    and duplicated it to handle when 
    1) The 'currentValue' of the element has not yet been determined
    namely handleEnableDisable_value_unknown
    2) When the 'currentValue' of the element has been determined
    namely handleEnableDisable_value_known

    Both functions are practically identical however
    because of time constraints and the risk of introducing any other bugs
    at this time-critical stage of my project,
    I have chosen not to refactor this code any further 
*/

const DEC = -1;
const INC = 1;
const RANGE_MIN = 2;
const RANGE_MAX = 98;
const BOOTSTRAP_MEDIUM_BREAKPOINT = 768;

// Solely handling #id_qty0_ values that is,
// IDs that are on the Poster Details Page
function handle_poster_details_ids(itemId, id_name, currentValue) {
    if (Number.isNaN(currentValue)) {
    // Erroneous value entered therefore reload the page 
        location.reload();
        return;
    }

    /* 
        Determine whether the value is greater than 99
        If true, then set value to 99 and disable the increment + button
    */
    if (currentValue > 99) {
        $(id_name).val(99);
        $(`#increment-qty0_${itemId}`).prop('disabled', true);
        return;
    }

    /* 
        Determine whether the value is less than 1
        If true, then set value to 1 and disable the decrement - button
    */
    if (currentValue < 1) {
        $(id_name).val(1);
        $(`#decrement-qty0_${itemId}`).prop('disabled', true);
        return;
    }       

    // For every one of these two conditions that are 'true'
    // 'Disable' the property else 'Enable' the property
    let minusDisabled = currentValue < RANGE_MIN;
    let plusDisabled = currentValue > RANGE_MAX;

    // Disable -/+ buttons related to #id_qty0_
    $(`#decrement-qty0_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-qty0_${itemId}`).prop('disabled', plusDisabled);
}

// Increment or Decrement #id_qty0_ values 
// That is, IDs that are on the Poster Details Page
function incdec_poster_details_ids(itemId, id_name, currentValue, incOrDec) {
    /* 
        Determine whether the value is greater than 98
        If true, then set value to 99 and disable the increment + button
    */
    if (currentValue == 98 && incOrDec == INC) {
            $(`#increment-qty0_${itemId}`).prop('disabled', true);
            return;
    }

    /* 
        Determine whether the value is less than 2
        If true, then set value to 1 and disable the - button
    */
    if (currentValue == 2 && incOrDec == DEC) {
            $(`#decrement-qty0_${itemId}`).prop('disabled', true);
            return true;
    }       

    // For every one of these two conditions that are 'true'
    // 'Disable' the property else 'Enable' the property
    let minusDisabled = currentValue < RANGE_MIN;
    let plusDisabled = currentValue > RANGE_MAX;

    // Disable -/+ buttons related to #id_qty0_
    $(`#decrement-qty0_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-qty0_${itemId}`).prop('disabled', plusDisabled);
}

// Enable all the +/- buttons for the Shopping Bag quantities of the ID in question
function enable_all(itemId) {
    $(`#decrement-qty1_${itemId}`).prop('disabled', false);
    $(`#decrement-qty2_${itemId}`).prop('disabled', false);
    $(`#increment-qty1_${itemId}`).prop('disabled', false);
    $(`#increment-qty2_${itemId}`).prop('disabled', false);
}

// Regarding BOTH #id_qty1_ and #id_qty2_
// For every one of these two conditions that are 'true'
// 'Disable' the property else 'Enable' the property
function enable_disable_buttons(itemId, currentValue) {
    let minusDisabled = currentValue < RANGE_MIN;
    let plusDisabled = currentValue > RANGE_MAX;
    $(`#decrement-qty1_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-qty1_${itemId}`).prop('disabled', plusDisabled);
    $(`#decrement-qty2_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-qty2_${itemId}`).prop('disabled', plusDisabled);
}

/* 
    Set value to 0 and disable the decrement - buttons 
    for BOTH #id_qty1_ and #id_qty2_
*/
function set_to_zero(itemId) {
    $(`#id_qty1_${itemId}`).val(0);
    $(`#id_qty2_${itemId}`).val(0);
    $(`#decrement-qty1_${itemId}`).prop('disabled', true);
    $(`#decrement-qty2_${itemId}`).prop('disabled', true);
}

/* 
    Set value to 99 and disable the increment + buttons 
    for BOTH #id_qty1_ and #id_qty2_
*/
function set_to_99(itemId) {
    $(`#id_qty1_${itemId}`).val(99);
    $(`#id_qty2_${itemId}`).val(99);
    $(`#increment-qty1_${itemId}`).prop('disabled', true);
    $(`#increment-qty2_${itemId}`).prop('disabled', true);
}

// Disable +/- buttons outside 1-99 range
function handleEnableDisable_value_unknown(itemId) {
    
    let matched_num = -1; // Catchall
    let id_name;
    for (let i=0; i<3; i++) {
        id_name = `#id_qty${i}_${itemId}`;

        if ($(id_name).length > 0) {

            /* Found matching #ID element
                #id_qty0_ corresponds to the Poster Details page
                #id_qty1_ corresponds to the Mobile/Tablet view of the Shopping Bag
                #id_qty2_ corresponds to the Desktop view of the Shopping Bag
            */

            matched_num = i; // this will be either 0 or 1
            break;
        }
    }

    // At this point, 'matched_num' ought to be either 0 or 1
    // This should not happen however just in case
    if (matched_num < 0) {
        return;
    }

    // Determine the current value of the #ID in question
    let currentValue = parseInt($(`#id_qty${matched_num}_${itemId}`).val());

    if (matched_num == 0) {
        // #id_qty0_ means that these IDs are on the Poster Details Page
        handle_poster_details_ids(itemId, id_name, currentValue);
        return;
    }

    // To begin with enable all the +/- buttons
    enable_all(itemId);

    // To begin with enable the decrement buttons
    $(`#decrement-qty1_${itemId}`).prop('disabled', false);
    $(`#decrement-qty2_${itemId}`).prop('disabled', false);
    
    /* Determine which is the correct ID/value to look at 
        by using the Bootstrap Breakpoint Value
        if width < 768 i.e. under MEDIUM - mobile - use #id_qty1_
        Otherwise use #id_qty2_
    */
    let window_width = window.innerWidth;
    if (window_width < BOOTSTRAP_MEDIUM_BREAKPOINT) {
        matched_num=1;
    } else {
        matched_num=2;
    }

    currentValue = parseInt($(`#id_qty${matched_num}_${itemId}`).val());

    if (Number.isNaN(currentValue)) {
    /* Erroneous value entered! Therefore reload the page 
        which in turn refreshes the original quantity values
    */
        location.reload();
        return;
    }

    /* 
        If the user has entered a value that is already too big
        Set value to 99 and disable the increment + buttons for BOTH #id_qty1_ and #id_qty2_
    */
    if (currentValue > 99) {
        set_to_99(itemId);
        return;
    }

    /* 
        If the user has entered a value that is already too small
        Set value to 0 and disable the decrement - buttons 
        for BOTH #id_qty1_ and #id_qty2_
    */
    if (currentValue < 0) {
        set_to_zero(itemId);
        return;
    }

    // Enable/Disable -/+ buttons accordingly depinding on their values
    // the elements that are related BOTH to #id_qty1_ and #id_qty2_
    enable_disable_buttons(itemId, currentValue);
    return;
}

// Disable +/- buttons outside 1-99 range
function handleEnableDisable_value_known(itemId, currentValue, incOrDec) {
    // Disable if either the currentValue is < 2 or > 97
    
    let matched_num = -1; // Catchall
    let id_name;
    let id_qty1_value;
    for (let i=0; i<3; i++) {
        id_name = `#id_qty${i}_${itemId}`;
        if ($(id_name).length > 0) {

            /* Found matching #ID element
                #id_qty0_ corresponds to the Poster Details page
                #id_qty1_ corresponds to the Mobile/Tablet view of the Shopping Bag
                #id_qty2_ corresponds to the Desktop view of the Shopping Bag
            */

            matched_num = i;
            id_qty1_value = parseInt($(id_name).val());
            break;
        }
    }

    // At this point, 'matched_num' ought to be either 0 or 1
    // This should not happen however just in case
    if (matched_num < 0) {
        return;
    }

    if (matched_num == 0) {
        // #id_qty0_ means that these IDs are on the Poster Details Page
        incdec_poster_details_ids(itemId, id_name, currentValue, incOrDec);
        return;
    }

    // 'currentValue' already determined
    if (Number.isNaN(currentValue)) {
    /* Erroneous value entered therefore reload the page 
        which in turn refreshes the original quantities
    */
        location.reload();
        return;
    }

    // To begin with enable all the +/- buttons
    enable_all(itemId);        

    if (id_qty1_value == -1) {
    /* Zero was entered
        Set value to 0 and disable the decrement - buttons 
        for BOTH #id_qty1_ and #id_qty2_
    */
        set_to_zero(itemId);
        return;
    }

    // To begin with enable all the +/- buttons
    enable_all(itemId);

    if (currentValue < 0) {
        // too low - set value to zero then disable decrement - buttons 
        // that are related BOTH to #id_qty1_ and #id_qty2_
        set_to_zero(itemId);
        return;
    }        

    /* 
        If the user has entered a value that is already too big
        set value to 99 and disable the increment + button
    */
    if (currentValue > 99) {
        // Set value to 99 and disable the increment + buttons 
        // for BOTH #id_qty1_ and #id_qty2_
        set_to_99(itemId);
        return;
    }
    
    /* Determine what is the updated value of 'currentValue'
        by using the Bootstrap Breakpoint Value
        if width < 768 i.e. under MEDIUM - mobile - use #id_qty1_
        Otherwise use #id_qty2_
    */
    let window_width = window.innerWidth;
    if (window_width < BOOTSTRAP_MEDIUM_BREAKPOINT) {
        matched_num=1;
    } else {
        matched_num=2;
    }

    // Enable/Disable the increment buttons depending on the updated value
    currentValue = parseInt($(`#id_qty${matched_num}_${itemId}`).val());

    // Enable/Disable -/+ buttons accordingly depinding on their values
    // the elements that are related BOTH to #id_qty1_ and #id_qty2_
    enable_disable_buttons(itemId, currentValue);
    return;
}

// Ensure proper enabling/disabling of all inputs on page load
let allQtyInputs = $('.qty_input');
for (let i = 0; i < allQtyInputs.length; i++) {
    let itemId = $(allQtyInputs[i]).data('item_id');
    handleEnableDisable_value_unknown(itemId);
}

// Check enable/disable every time the input is changed
$('.qty_input').change(function() {
    let itemId = $(this).data('item_id');
    handleEnableDisable_value_unknown(itemId);
});

// Increment quantity
$('.increment-qty').click(function(e) {
    e.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    let itemId = $(this).data('item_id');
    handleEnableDisable_value_known(itemId, currentValue, INC);
});

// Decrement quantity
$('.decrement-qty').click(function(e) {
    e.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    let itemId = $(this).data('item_id');
    handleEnableDisable_value_known(itemId, currentValue, DEC);
});

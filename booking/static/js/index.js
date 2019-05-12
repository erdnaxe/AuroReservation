// SPDX-License-Identifier: GPL-2.0-or-later

import {Calendar} from '@fullcalendar/core';
import resourceTimelinePlugin from '@fullcalendar/resource-timeline';
import '@fullcalendar/core/main.css';
import '@fullcalendar/timeline/main.css';
import '@fullcalendar/resource-timeline/main.css';
import frLocale from '@fullcalendar/core/locales/fr';
import esLocale from '@fullcalendar/core/locales/es';
import tippy from 'tippy.js'

document.addEventListener('DOMContentLoaded', function () {
    let calendarEl = document.getElementById('calendar');
    let calendar = new Calendar(calendarEl, {
        schedulerLicenseKey: 'GPL-My-Project-Is-Open-Source',
        plugins: [resourceTimelinePlugin],
        timeZone: 'Europe/Paris',
        defaultView: 'resourceTimelineWeek',
        resourceLabelText: '\ ',
        nowIndicator: true,
        slotLabelInterval: '04:00:00',
        resourceAreaWidth: "20%",
        header: {
            left: '',
            center: 'title',
            right: 'today prev,next resourceTimelineDay,resourceTimelineWeek'
        },
        height: "auto",
        locales: [frLocale, esLocale],
        resources: 'fc/resources.json',
        events: 'fc/events.json',
        resourceRender: function (renderInfo) {
            const cellText = renderInfo.el.querySelector('.fc-cell-text');

            // Link to add a reservation
            if (renderInfo.resource.extendedProps.add_url) {
                cellText.style.color = "#447e9b";
                cellText.style.fontWeight = "bold";
                cellText.style.cursor = 'pointer';
                cellText.addEventListener('click', function () {
                    window.location.href = renderInfo.resource.extendedProps.add_url;
                });
            }

            // Tooltip
            if (renderInfo.resource.extendedProps.comment) {
                new tippy(cellText, {
                    content: renderInfo.resource.extendedProps.comment.replace(/\n/g, "<br />"),
                    placement: 'right',
                    arrow: true,
                    boundary: 'window',
                });
            }
        },
        eventRender: function (renderInfo) {
            renderInfo.el.style.color = 'white';
            const cellText = renderInfo.el.querySelector('.fc-content');

            // Tooltip
            if (renderInfo.event.extendedProps.comment) {
                new tippy(renderInfo.el, {
                    content: renderInfo.event.extendedProps.comment,
                    placement: 'top',
                    arrow: true,
                });
            }
        }
    });

    calendar.render();

    // Switch locale with Django locale
    calendar.setOption('locale', document.documentElement.lang);

    // Scroll to now
    setTimeout(function () {
        let today = document.querySelector('.fc-now-indicator');
        let scroller = document.getElementsByClassName('fc-scroller')[1];
        scroller.scrollLeft = today.offsetLeft;
    }, 10);
});

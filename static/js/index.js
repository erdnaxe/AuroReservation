// SPDX-License-Identifier: GPL-2.0-or-later

import {Calendar} from '@fullcalendar/core';
import resourceTimelinePlugin from '@fullcalendar/resource-timeline';
import '@fullcalendar/core/main.css';
import '@fullcalendar/timeline/main.css';
import '@fullcalendar/resource-timeline/main.css';
import frLocale from '@fullcalendar/core/locales/fr';
import tippy from 'tippy.js'

document.addEventListener('DOMContentLoaded', function () {
    let calendarEl = document.getElementById('calendar');

    let calendar = new Calendar(calendarEl, {
        schedulerLicenseKey: 'GPL-My-Project-Is-Open-Source',
        plugins: [resourceTimelinePlugin],
        timeZone: 'UTC',
        defaultView: 'resourceTimelineWeek',
        editable: false,
        resourceLabelText: 'Rooms',
        nowIndicator: true,
        slotDuration: '01:00:00',
        slotLabelInterval: '03:00:00',
        resourceAreaWidth: "20%",
        header: {
            left: '',
            center: 'title',
            right: 'prev,next resourceTimelineDay,resourceTimelineWeek'
        },
        height: "auto",
        locales: [frLocale],
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
                    content: renderInfo.resource.extendedProps.comment,
                    placement: 'right',
                    arrow: true,
                });
            }
        }
    });

    calendar.render();

    // TODO: switch locale with Django locale
    calendar.setOption('locale', 'fr');
});

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
        defaultView: 'resourceTimelineDay',
        editable: false,
        resourceLabelText: 'Rooms',
        header: {
            left: 'prev,next',
            center: 'title',
            right: 'resourceTimelineDay,resourceTimelineWeek'
        },
        height: "auto",
        locales: [frLocale],
        resources: 'fc/resources.json',
        events: 'fc/events.json',
        resourceRender: function (renderInfo) {
            const questionMark = document.createElement('strong');
            questionMark.innerText = ' (?) ';
            renderInfo.el.querySelector('.fc-cell-text').appendChild(questionMark);
            const tooltip = new tippy(questionMark, {
                content: renderInfo.resource.extendedProps.comment,
                placement: 'right',
                arrow: true,
            });
        }
    });

    calendar.render();

    // TODO: switch locale with Django locale
    calendar.setOption('locale', 'fr');
});

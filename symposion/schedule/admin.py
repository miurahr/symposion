from __future__ import unicode_literals
from django.contrib import admin

from symposion.schedule.models import Schedule, Day, Room, SlotKind, Slot, SlotRoom, Presentation


class DayInline(admin.StackedInline):
    model = Day
    extra = 2


class SlotKindInline(admin.StackedInline):
    model = SlotKind


class ScheduleAdmin(admin.ModelAdmin):
    model = Schedule
    inlines = [DayInline, SlotKindInline, ]


class SlotRoomInline(admin.TabularInline):
    model = SlotRoom
    extra = 1


class SlotAdmin(admin.ModelAdmin):
    list_filter = ("day", "kind")
    list_display = ("day", "start", "end", "kind", "content")
    inlines = [SlotRoomInline, ]


class RoomAdmin(admin.ModelAdmin):
    inlines = [SlotRoomInline, ]


class PresentationAdmin(admin.ModelAdmin):
    model = Presentation
    list_filter = ("section", "cancelled", "slot")
    readonly_fields = ("title", "speaker", "abstract", "description")
    fieldsets = (
        (None, {
          'fields': ("section", "slot", "proposal_base")
        }),
        ('Proposal Details', {
          'fields': ("title", "speaker", "abstract", "description")
        }),
    )


admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Slot, SlotAdmin)
admin.site.register(Presentation, PresentationAdmin)

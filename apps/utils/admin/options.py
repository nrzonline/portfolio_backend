from django.contrib.admin.options import ModelAdmin
from django.core.exceptions import ObjectDoesNotExist


class ModelAdminSaveUserOnCreate(ModelAdmin):
    """
        This mixin should be used to automatically save request.user
        to the model's user field. Throws FieldDoesNotExist
        if the `user` field is not available in the model.
    """

    def __init__(self, *args, **kwargs):
        super(ModelAdminSaveUserOnCreate, self).__init__(*args, **kwargs)

    """
        Setting the user field of the model when creating a new object if
        the user field is available.
    """
    def save_model(self, request, obj, form, change):
        if not change:
            if obj._meta.get_field('user'):
                obj.user = request.user
                obj.save()

    """
        Setting the user field of the admin Inline formsets their models,
        if there is a `user` field available and the field as not yet
        been set.
    """
    def save_formset(self, request, form, formset, change):
        for iteration_form in formset.forms:
            obj = iteration_form.instance
            if obj._meta.get_field('user'):

                # Make sure the user is only set when the object is new
                try:
                    if obj.user:
                        pass
                except ObjectDoesNotExist:
                    obj.user = request.user
        formset.save()



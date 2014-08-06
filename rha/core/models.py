# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


STATE_CHOICES = (
    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AP', u'Amapá'),
    ('AM', u'Amazonas'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MT', u'Mato Grosso'),
    ('MS', u'Mato Grosso do Sul'),
    ('MG', u'Minas Gerais'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PR', u'Paraná'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RS', u'Rio Grande do Sul'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('SC', u'Santa Catarina'),
    ('SP', u'São Paulo'),
    ('SE', u'Sergipe'),
    ('TO', u'Tocantins'),
)

ICON_CHOICES = (
    ('fa-user-md', u'Profissional'),
    ('fa-flag-checkered', u'Bandeira'),
    ('fa-dollar', u'Sifrão'),
    ('fa-graduation-cap', u'Graduação'),
)

MODULE_CHOICES = (
    ('MLV', u'Módulo Laboratorial (à vista)'),
    ('MLP', u'Módulo Laboratorial (à prazo)'),
    ('MCV', u'Módulo Clínico (à vista)'),
    ('MCP', u'Módulo Clínico (à prazo)'),
)

TRUE_FALSE_CHOICES = (
    ('N', u'Não'),
    ('S', u'Sim'),
)


class Enterprise(models.Model):
    name = models.CharField(_(u'Nome'), max_length=100)
    description = models.CharField(_(u'Descrição'), max_length=100,
                                   blank=True, null=True)
    cnpj = models.CharField(_(u'CNPJ'), max_length=20,
                            help_text='99.999.999/9999-99',
                            blank=True, null=True)
    address = models.CharField(_(u'Endereço'), max_length=200,
                               blank=True, null=True)
    number = models.CharField(_(u'Número'), max_length=10,
                              blank=True, null=True)
    complement = models.CharField(_(u'Complemento'), max_length=100,
                                  blank=True, null=True)
    cep = models.CharField(_(u'CEP'), max_length=9, help_text='99999-999',
                           blank=True, null=True)
    district = models.CharField(_(u'Bairro'), max_length=100,
                                blank=True, null=True)
    city = models.CharField(_(u'Cidade'), max_length=100)
    state = models.CharField(_(u'UF'), max_length=2, choices=STATE_CHOICES)
    country = models.CharField(_(u'País'), max_length=50)
    phone1 = models.CharField(_(u'Fone 1'), max_length=20,
                              help_text='(99) 9999-9999')
    phone2 = models.CharField(_(u'Fone 2'), max_length=20,
                              help_text='(99) 9999-9999', blank=True, null=True)
    phone3 = models.CharField(_(u'Fone 3'), max_length=20,
                              help_text='(99) 9999-9999', blank=True, null=True)
    email = models.EmailField(_(u'Email'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Empresa')
        verbose_name_plural = _(u'Empresa')


class Contact(models.Model):
    content = models.CharField(_(u'Conteúdo'), max_length=200,
                               help_text='Mensagem para área de contato')

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = _(u'Contato')
        verbose_name_plural = _(u'Contato')


class Partner(models.Model):
    name = models.CharField(_(u'Nome'), max_length=100)
    image = models.ImageField(_(u'Logo'), upload_to='partners')
    link = models.URLField(_(u'Site'), blank=True, null=True)

    def admin_image(self):
        return '<img src="%s" width="60" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = u'Logo'

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Parceiro')
        verbose_name_plural = _(u'Parceiros')


class Step(models.Model):
    icon = models.CharField(_(u'Ícone'), max_length=20, choices=ICON_CHOICES)
    title = models.CharField(_(u'Título'), max_length=25)
    description = models.CharField(_(u'Descrição'), max_length=130)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u'Proposta de Valor')
        verbose_name_plural = _(u'Propostas de Valor')


class Gallery(models.Model):
    name = models.CharField(_(u'Nome'), max_length=100)
    image = models.ImageField(_(u'Imagem'), upload_to='gallery')

    def admin_image(self):
        return '<img src="%s" width="60" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = u'Imagem'

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Galeria')
        verbose_name_plural = _(u'Galeria')


class Course(models.Model):
    description = models.CharField(_(u'Descrição'), max_length=170)

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name = _(u'Curso')
        verbose_name_plural = _(u'Curso')


class Objective(models.Model):
    description = models.CharField(_(u'Descrição'), max_length=125)

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name = _(u'Objetivo')
        verbose_name_plural = _(u'Objetivos')


class Public(models.Model):
    description = models.CharField(_(u'Descrição'), max_length=170)

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name = _(u'Público')
        verbose_name_plural = _(u'Público')


class Team(models.Model):
    name = models.CharField(_(u'Nome'), max_length=30)
    description = models.CharField(_(u'Descrição'), max_length=60)
    link = models.URLField(_(u'Currículo'), blank=True, null=True)
    image = models.ImageField(_(u'Foto'), upload_to='team',
                              blank=True, null=True)

    def admin_image(self):
        if self.image.url:
            return '<img src="%s" width="60" />' % self.image.url
        else:
            return '<img src="teste.jpg" width="60" />'
    admin_image.allow_tags = True
    admin_image.short_description = u'Foto'

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Professor')
        verbose_name_plural = _(u'Professores')
        ordering = ['name']


class Cost(models.Model):
    title = models.CharField(_(u'Título do Módulo'), max_length=30)
    price1 = models.DecimalField(_(u'Valor (à vista)'),
                                 decimal_places=2, max_digits=10)
    description1 = models.CharField(_(u'Descrição (à vista)'), max_length=100)
    price2 = models.DecimalField(_(u'Valor (à prazo)'),
                                 decimal_places=2, max_digits=10)
    description2 = models.CharField(_(u'Descrição (à prazo)'), max_length=130)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u'Preço')
        verbose_name_plural = _(u'Preços')


class Graduation(models.Model):
    name = models.CharField(_(u'Graduação'), max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Graduação')
        verbose_name_plural = _(u'Graduações')


class Institute(models.Model):
    name = models.CharField(_(u'Instituição'), max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Instituição')
        verbose_name_plural = _(u'Instituições')


class Subscribe(models.Model):
    subscribe_date = models.DateTimeField(_(u'Data de Inscrição'),
                                          auto_now_add=True)
    module = models.CharField(_(u'Módulo'), max_length=10,
                              choices=MODULE_CHOICES)
    name = models.CharField(_(u'Nome'), max_length=200)
    cpf = models.CharField(_(u'CPF'), max_length=20)
    email = models.EmailField(_(u'E-mail'))
    mobile = models.CharField(_(u'Celular'), max_length=20)
    phone = models.CharField(_(u'Fixo'), max_length=20, blank=True, null=True)
    cep = models.CharField(_(u'CEP'), max_length=9)
    address = models.CharField(_(u'Endereço'), max_length=200)
    number = models.IntegerField(_(u'Número'))
    complement = models.CharField(_(u'Complemento'), max_length=200,
                                  blank=True, null=True)
    district = models.CharField(_(u'Bairro'), max_length=100)
    city = models.CharField(_(u'Cidade'), max_length=100)
    state = models.CharField(_(u'UF'), max_length=2, choices=STATE_CHOICES)
    graduation = models.ForeignKey(Graduation, verbose_name=u'Graduação',
                                   related_name=u'GraName')
    year_conclusion = models.CharField(_(u'Ano de Conclusão'), max_length=4)
    institute = models.ForeignKey(Institute, verbose_name=u'Instituição',
                                  related_name=u'InsName')
    special = models.CharField(_(u'Necessidades Especiais?'), max_length=1,
                               choices=TRUE_FALSE_CHOICES)
    which = models.CharField(_(u'Qual Necessidade Especial Você Tem?'),
                             max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Inscrição')
        verbose_name_plural = _(u'Inscrições')
